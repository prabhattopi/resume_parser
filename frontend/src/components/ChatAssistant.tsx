import { useState } from "react";
import axios from "axios";

const ChatAssistant = () => {
  const [messages, setMessages] = useState<{ role: string; text: string }[]>([]);
  const [input, setInput] = useState("");

  // ✅ Safely parse stored data
  const storedData = localStorage.getItem("data");
  const data = storedData ? JSON.parse(storedData) : null;
  const resumeId = data?._id || null;

  const handleSend = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", text: input }];
    setMessages(newMessages);

    try {
      // ✅ Ensure `resume_id` is not `null`
      const payload = resumeId ? { message: input, resume_id: resumeId } : { message: input };

      const response = await axios.post("http://localhost:5000/api/analysis/chat", payload);

      setMessages([...newMessages, { role: "assistant", text: response.data.reply }]);
    } catch {
      setMessages([...newMessages, { role: "assistant", text: "Error fetching response. Try again!" }]);
    }

    setInput("");
  };

  return (
    <div className="max-w-lg mx-auto mt-8 p-4 bg-gray-100 shadow-lg rounded-lg">
      <h2 className="text-lg font-bold mb-3">Career Assistant Chat</h2>
      <div className="h-64 overflow-y-auto bg-white p-3 border rounded-lg">
        {messages.map((msg, idx) => (
          <p key={idx} className={`p-2 rounded ${msg.role === "user" ? "bg-blue-300" : "bg-gray-300"}`}>
            <strong>{msg.role === "user" ? "You" : "AI"}:</strong> {msg.text}
          </p>
        ))}
      </div>
      <div className="flex mt-3">
        <input
          className="flex-1 border p-2 rounded-l-lg"
          placeholder="Ask career-related questions..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="bg-blue-500 text-white p-2 rounded-r-lg" onClick={handleSend} disabled={!resumeId}>
          {resumeId ? "Send" : "Upload Resume First"}
        </button>
      </div>
    </div>
  );
};

export default ChatAssistant;
