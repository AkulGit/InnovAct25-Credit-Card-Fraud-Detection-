document.getElementById("fraudForm").addEventListener("submit", function(event) {
  event.preventDefault();

  // Collect input values
  const amount = document.getElementById("amount").value;
  const time = document.getElementById("time").value;
  const location = document.getElementById("location").value;
  const merchant = document.getElementById("merchant").value;

  // Here, you would send data to Flask/Python model
  // For now, simulate fraud detection:
  let resultText = "";

  if (amount > 1000) {
    resultText = "⚠️ High Fraud Risk";
    document.getElementById("result").style.color = "red";
  } else {
    resultText = "✅ Transaction Looks Safe";
    document.getElementById("result").style.color = "green";
  }

  document.getElementById("result").innerText = resultText;
});
