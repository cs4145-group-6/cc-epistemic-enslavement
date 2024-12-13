import React, { useState } from "react";

interface YesNoQuestionProps {
  question: string; // The question to display
}

const YesNoQuestion: React.FC<YesNoQuestionProps> = ({ question }) => {
  const [answer, setAnswer] = useState<string | null>(null);

  const handleAnswer = (response: string) => {
    setAnswer(response);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "20px" }}>
      <h2>{question}</h2>
      <div>
        <button
          onClick={() => handleAnswer("Yes")}
          style={{ marginRight: "10px", padding: "10px 20px" }}
        >
          Yes
        </button>
        <button
          onClick={() => handleAnswer("No")}
          style={{ padding: "10px 20px" }}
        >
          No
        </button>
      </div>
      {answer && (
        <p style={{ marginTop: "20px", fontSize: "16px" }}>
          You answered: <strong>{answer}</strong>
        </p>
      )}
    </div>
  );
};

export default YesNoQuestion;
