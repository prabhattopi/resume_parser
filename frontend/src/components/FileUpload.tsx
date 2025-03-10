import { useState } from "react";
import axios from "axios";

const FileUpload = ({ onUploadSuccess }: { onUploadSuccess: (data: any) => void }) => {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file.");
      return;
    }

    setUploading(true);
    setError("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:5000/api/resume/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      
      onUploadSuccess(response.data);
      localStorage.setItem("data", JSON.stringify(response.data?.data))

    } catch (err) {
      setError("Error uploading file. Please try again.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow-md">
      <input type="file" accept=".pdf,.docx" onChange={handleFileChange} className="mb-2" />
      <button
        onClick={handleUpload}
        className="px-4 py-2 bg-blue-500 text-white rounded-lg disabled:opacity-50"
        disabled={uploading}
      >
        {uploading ? "Uploading..." : "Upload Resume"}
      </button>
      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
};

export default FileUpload;
