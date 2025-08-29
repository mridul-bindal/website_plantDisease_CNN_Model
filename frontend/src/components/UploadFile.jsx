import { useState } from "react";
import axios from "axios";
import "./UploadFile.css";

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [message, setMessage] = useState("");
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
      setMessage("");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setUploading(true);
    setMessage("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage(
        `Prediction: ${res.data.predicted_label} (Confidence: ${(res.data.confidence * 100).toFixed(2)}%)`
      );
    } catch (err) {
      console.error(err);
      setMessage("Upload failed");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload an Image</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        {preview && (
          <div className="upload-preview">
            <img src={preview} alt="Preview" />
          </div>
        )}
        <button className="upload-button" type="submit" disabled={uploading}>
          {uploading ? "Uploading..." : "Upload & Predict"}
        </button>
      </form>
      {message && <p className="upload-message">{message}</p>}
    </div>
  );
}
