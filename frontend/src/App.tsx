import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import UploadPage from "./pages/Upload";
import FeedbackPage from "./pages/Feedback";
import CareerAdvicePage from "./pages/CareerAdvice";

function App() {
  return (
    <Router>
      <nav className="p-4 bg-blue-500 text-white flex gap-4">
        <Link to="/">Upload Resume</Link>
        {/* <Link to="/feedback">AI Feedback</Link> */}
        <Link to="/career-advice">Career Advice</Link>
      </nav>

      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/feedback" element={<FeedbackPage />} />
        <Route path="/career-advice" element={<CareerAdvicePage />} />
      </Routes>
    </Router>
  );
}

export default App;
