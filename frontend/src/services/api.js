export async function predictChurn(payload) {
  const res = await fetch("http://127.0.0.1:8000/predict-churn", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  return await res.json();
}