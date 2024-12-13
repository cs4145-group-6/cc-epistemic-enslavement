import React, { useState } from "react";

interface YesNoQuestionProps {
  question: string; // The question to display
}

const YesNoQuestion: React.FC<YesNoQuestionProps> = ({ question }) => {
  const [answer, setAnswer] = useState<string | null>(null);
  const [responseMessage, setResponseMessage] = useState<string | null>(null);

  const handleAnswer = async (response: string) => {
    setAnswer(response);

    try {
      const res = await fetch("https://backend-q53g.onrender.com/submit-answer", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ answer: response }),
      });

      if (res.ok) {
        const data = await res.json();
        setResponseMessage(data.message); // e.g., "Answer recorded successfully!"
      } else {
        const error = await res.json();
        setResponseMessage(error.error || "Failed to submit answer.");
      }
    } catch (error) {
      setResponseMessage("An error occurred while submitting your answer.");
    }
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
      {responseMessage && (
        <p style={{ marginTop: "20px", color: "green" }}>{responseMessage}</p>
      )}
    </div>
  );
};

export default YesNoQuestion;
