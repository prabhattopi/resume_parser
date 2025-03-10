import { useState } from "react";
import FileUpload from "../components/FileUpload";
import ResumeFeedback from "../components/ResumeFeedback";

const UploadPage = () => {
  const storedData = localStorage.getItem("data");
  const data = storedData ? JSON.parse(storedData) : null;
  const resume_id = data?._id || null;
  console.log(resume_id)
  const [resumeId, setResumeId] = useState<string | null>(resume_id||null);

  return (
    <div className="max-w-xl mx-auto mt-10">
      <h1 className="text-2xl font-bold">Upload Your Resume</h1>
      <FileUpload onUploadSuccess={(data) => setResumeId(data.data._id)} />
      {resumeId && <ResumeFeedback resumeId={resumeId} />}
    </div>
  );
};

export default UploadPage;
