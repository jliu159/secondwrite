import React, { useEffect, useState } from "react";
import "../style.css"; //@ts-ignore
import JsonTable from "./JsonTable";
import { useDownloadMutation } from "../api/apiSlice";
import Header from "./Header";
import { useNavigate } from "react-router-dom";

const Review: React.FC = () => {
  const navigate = useNavigate();
  const [download, { data }] = useDownloadMutation();

  const [jsonData, setJsonData] = useState([]);

  useEffect(() => {
    download({});
  }, []);

  console.log(data)

  useEffect(() => {
    if (!data) return;
    setJsonData(data)
  }, [data])

  // download the json file
  const handleDownload = () => {
    // Convert JSON data to a string
    const jsonString = JSON.stringify(jsonData, null, 2);

    // Create a Blob from the JSON string
    const blob = new Blob([jsonString], { type: "application/json" });

    // Create a URL for the Blob
    const url = URL.createObjectURL(blob);

    // Create an anchor element and set its href to the Blob URL
    const a = document.createElement("a");
    a.href = url;
    a.download = "data.json"; // Set the downloaded file name
    document.body.appendChild(a);

    // Programmatically click the anchor to trigger the download
    a.click();

    // Clean up the URL object and remove the anchor
    URL.revokeObjectURL(url);
    document.body.removeChild(a);
  };

  return (
    <div>
      <Header currentStep="review" />
      <div className='nav-buttons' style={{paddingTop: 0, paddingBottom: '10px', justifyContent: 'center'}}>
        <button className='back-btn' onClick={() => navigate('/upload')}>
          Back
        </button>
        <button onClick={handleDownload} className="continue-btn">
          Download
        </button>
      </div>
      <JsonTable jsonData={jsonData} />
    </div>
  );
};

export default Review;
