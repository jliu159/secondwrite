import React from "react";

//@ts-ignore
function JsonTable({ jsonData }) {
  //@ts-ignore
  const renderTreeRows = (nodes, depth = 0) => { //@ts-ignore
    return nodes.map((node) => (
      <React.Fragment key={node.id}>
        <tr>
          <td style={{ paddingLeft: `${depth * 30}px` }}>{node.name || ""}</td>
          <td>{node.process_id || ""}</td>
          <td>{node.start_time || ""}</td>
          <td>{node.user || ""}</td>
          <td>{node.path || ""}</td>
          <td>{node.vendor || ""}</td>
          <td>{node.version || ""}</td>
          <td>{node.pe_name || ""}</td>
          <td>{node.pe_version || ""}</td>
          <td>{node.modified_time || ""}</td>
        </tr>
        {/* Recursively render children, increasing the depth */}
        {node.children && renderTreeRows(node.children, depth + 1)}
      </React.Fragment>
    ));
  };

  return (
    <table border={1} style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          <th>Name</th>
          <th>PID</th>
          <th>Start Time</th>
          <th>User</th>
          <th>Path</th>
          <th>Vendor</th>
          <th>Version</th>
          <th>PE Name</th>
          <th>PE Version</th>
          <th>Modified Time</th>
        </tr>
      </thead>
      <tbody>{renderTreeRows(jsonData)}</tbody>
    </table>
  );
}

export default JsonTable;
