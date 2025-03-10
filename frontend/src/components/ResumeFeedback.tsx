import { useEffect, useState } from "react";
import axios from "axios";

const ResumeFeedback = ({ resumeId }: { resumeId: string }) => {
  const [feedback, setFeedback] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/analysis/feedback/${resumeId}`)
      .then(response => setFeedback(response.data.feedback))
      .catch(() => setFeedback(null))
      .finally(() => setLoading(false));
  }, [resumeId]);

  if (loading) return <p>Loading feedback...</p>;

  return (
    <div className="p-4 bg-gray-100 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold">AI Feedback</h2>
      {feedback ? (
        <ul>
          <li><strong>Skills:</strong> {feedback.strengths.join(", ")}</li>
          <li><strong>Experience:</strong> {feedback.experience.join(", ")}</li>
          <li><strong>Suggestions:</strong></li>
          <ul className="list-disc pl-6">
            {feedback.suggestions.map((s: string, index: number) => <li key={index}>{s}</li>)}
          </ul>
        </ul>
      ) : (
        <p>No feedback available.</p>
      )}
    </div>
  );
};

export default ResumeFeedback;
