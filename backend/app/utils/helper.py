import events_pb2
from database.database import Base, engine, Session
from models.models import Process, Application, PeFile, User, Message

def upload_to_sql(session, file_content):
    # Deserialize the binary content into the protobuf message
    message = events_pb2.Message()
    message.ParseFromString(file_content)

    # delete all tables
    for table in Base.metadata.tables.values():
        session.query(table).delete()
    session.commit()

    # INSERT RECORDS INTO SQLITE
    # Insert processes
    for process in message.processes:
        try:
            new_process = Process(
                id=process.id,
                parent_process_id=process.parent_process_id,
                process_id=process.process_id,
                start_time=process.start_time,
                user_id=process.user_id,
                application_id=process.application_id,
            )
            session.add(new_process)
            session.commit()
        except Exception as e:
            session.rollback()  # Rollback the transaction
            print(f"Error committing process with ID {process.id}: {e}")

    # Insert applications
    for application in message.applications:
        new_application = Application(
            id=application.id,
            pe_file_id=application.pe_file_id,
            name=application.name,
            vendor=application.vendor,
            version=application.version,
        )
        session.add(new_application)
        session.commit()

    # Insert pe_files
    for pe_file in message.pe_files:
        new_pe_file = PeFile(
            id=pe_file.id,
            sha256=pe_file.sha256,
            name=pe_file.name,
            path=pe_file.path,
            modified_time=pe_file.modified_time,
            version=pe_file.version,
        )
        session.add(new_pe_file)
        session.commit()

    # Insert users
    for user in message.users:
        new_user = User(
            id=user.id,
            security_identifier=user.security_identifier,
            username=user.username,
            domain=user.domain,
        )
        session.add(new_user)
        session.commit()

    # Insert Message record (if necessary)
    new_message = Message(
        process_ids=', '.join([str(p.id) for p in message.processes]),
        application_ids=', '.join([str(a.id) for a in message.applications]),
        pe_file_ids=', '.join([str(p.id) for p in message.pe_files]),
        user_ids=', '.join([str(u.id) for u in message.users]),
    )
    session.add(new_message)
    session.commit()
    session.close()


# Function to find the highest parent for a process
def find_highest_parent(process, process_dict):
    # Traverse up to find the root
    while process["parent_process_id"]:
        parent_process = process_dict.get(process["parent_process_id"])
        if parent_process:
            process = parent_process
        else:
            break
    return process


def build_json(session):
    def find_highest_parent(process, process_dict):
        """
        Recursively finds the highest parent process in the tree.
        If the parent_process_id doesn't exist in the data, returns the current process.
        """
        while process.get("parent_process_id") in process_dict:
            process = process_dict[process["parent_process_id"]]
        return process

    try:
        # Fetch all data from the tables
        processes = session.query(Process).all()
        applications = session.query(Application).all()
        pe_files = session.query(PeFile).all()
        users = {user.id: user for user in session.query(User).all()}  # Build a dictionary for fast lookup

        # Build a tree structure
        process_dict = {}
        for process in processes:
            # Look up the user information
            user_info = users.get(process.user_id)
            user_display = f"{user_info.domain}\\{user_info.username}" if user_info else "Unknown"

            process_data = {
                "id": process.id,
                "parent_process_id": process.parent_process_id,
                "process_id": process.process_id,
                "start_time": process.start_time,
                "user": user_display,  # Add user information here
                "application_id": process.application_id,
            }

            # Add applications related to this process
            for app in applications:
                if app.id and process.application_id and app.id == process.application_id:
                    process_data.update({
                        "name": app.name,
                        "vendor": app.vendor,
                        "version": app.version,
                        "pe_file_id": app.pe_file_id,
                    })
                                # Add applications related to this process
                for pe_file in pe_files:
                    if pe_file.id and app.pe_file_id and pe_file.id == app.pe_file_id:
                        process_data.update({
                            "pe_name": pe_file.name,
                            "path": pe_file.path,
                            "pe_version": pe_file.version,
                            "modified_time": pe_file.modified_time,
                        })


            process_dict[process.process_id] = process_data

        # Create the tree structure by nesting processes based on parent_process_id
        tree = []
        visited = set()

        for process in process_dict.values():
            highest_parent = find_highest_parent(process, process_dict)
            if highest_parent["process_id"] not in visited:
                visited.add(highest_parent["process_id"])
                tree.append(highest_parent)

            if "children" not in highest_parent:
                highest_parent["children"] = []

            if process != highest_parent:
                highest_parent["children"].append(process)

        return tree

    finally:
        session.close()
