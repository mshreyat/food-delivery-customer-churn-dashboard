import { useState } from "react";
import { predictChurn } from "../services/api";

const options = [
  "Strongly disagree",
  "Disagree",
  "Neutral",
  "Agree",
  "Strongly agree"
];

function Prediction() {
  const [form, setForm] = useState({
    Age: 28,
    Family_size: 3,
    Late_Delivery: "Disagree",
    Poor_Hygiene: "Disagree",
    Bad_past_experience: "Disagree",
    Long_delivery_time: "Disagree",
    More_Offers_and_Discount: "Agree",
    Good_Food_quality: "Strongly agree",
    Ease_and_convenient: "Strongly agree"
  });

  const [result, setResult] = useState("");

  const handleChange = (field, value) => {
    setForm({ ...form, [field]: value });
  };

  const handlePredict = async () => {
  try {
    const data = await predictChurn(form);
    console.log("API RESPONSE:", data);
    setResult(data.prediction || "No prediction returned");
  } catch (error) {
    console.error(error);
    setResult("Backend connection failed");
  }
};

  const surveyFields = [
    "Late_Delivery",
    "Poor_Hygiene",
    "Bad_past_experience",
    "Long_delivery_time",
    "More_Offers_and_Discount",
    "Good_Food_quality",
    "Ease_and_convenient"
  ];

  return (
    <div style={{ maxWidth: "700px", margin: "40px auto", padding: "20px" }}>
      <h1>🍔 Food Delivery Churn Prediction</h1>

      <div style={{ marginBottom: "15px" }}>
        <label>Age: </label>
        <input
          type="number"
          value={form.Age}
          onChange={(e) => handleChange("Age", Number(e.target.value))}
        />
      </div>

      <div style={{ marginBottom: "15px" }}>
        <label>Family Size: </label>
        <input
          type="number"
          value={form.Family_size}
          onChange={(e) =>
            handleChange("Family_size", Number(e.target.value))
          }
        />
      </div>

      {surveyFields.map((field) => (
        <div key={field} style={{ marginBottom: "15px" }}>
          <label>{field.replaceAll("_", " ")}: </label>
          <select
            value={form[field]}
            onChange={(e) => handleChange(field, e.target.value)}
          >
            {options.map((opt) => (
              <option key={opt}>{opt}</option>
            ))}
          </select>
        </div>
      ))}

      <button
        onClick={handlePredict}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer"
        }}
      >
        Predict Churn
      </button>

      {result && (
        <h2 style={{ marginTop: "20px" }}>
          Prediction: {result}
        </h2>
      )}
    </div>
  );
}

export default Prediction;