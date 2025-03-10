import ChatAssistant from "../components/ChatAssistant";

const CareerAdvicePage = () => {
  return (
    <div className="max-w-xl mx-auto mt-10">
      <h1 className="text-2xl font-bold">Career Advice</h1>
      <p className="mt-2 text-gray-600">
        Get personalized career guidance from our AI-powered assistant.
      </p>
      <ChatAssistant />
    </div>
  );
};

export default CareerAdvicePage;
