// components/Upload.js
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "./Header";
import { useUploadMutation } from "../api/apiSlice";

const Upload = () => {
  const navigate = useNavigate();
  const [file, setFile] = useState<File | null>(null);
  const [upload] = useUploadMutation();

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please choose a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    await upload({'formData': formData})

    navigate('/review')
  }

  return (
    <div className="step-container">
      <Header currentStep="upload" />
      <h2>Upload a Binary File</h2>
      <input type="file" onChange={handleFileChange} />
      <div className="nav-buttons">
        <button onClick={handleUpload} className="continue-btn">
          Upload
        </button>
      </div>
    </div>
  );
};

export default Upload;
