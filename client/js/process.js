document.getElementById("start").addEventListener("click", async () => {
  var typeChosen = document.querySelector(
    'input[name="question1"]:checked'
  ).value;

  var nullValues = document.querySelector(
    'input[name="question2"]:checked'
  ).value;

  var SmoteChosen = document.querySelector(
    'input[name="question3"]:checked'
  ).value;

  var ScalerChosen = document.querySelector(
    'input[name="question4"]:checked'
  ).value;

  var target = document.querySelector('input[name="target"]').value;
  var splitPer = document.querySelector('input[name="splitPer"]').value;

  //validation

  //to send to the server
  var data = {
    target: target,
    type: typeChosen,
    fill_null: nullValues,
    split_percent: splitPer,
    can_apply_smote: SmoteChosen == "true" ? true : false,
    scaler: ScalerChosen,
  };
  responseData = await process(data);

  //graphs and output:
  if (typeChosen == "Regression") {
    MAE(responseData);
    MAPE(responseData);
    MSE(responseData);
    r2score(responseData);
  }
});

//fucntion to fetch
const process = async (data) => {
  await fetch("http://localhost:5000/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    mode: "cors",
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((response) => {
      console.log(JSON.stringify(response));
      responseData = response;
    })
    .catch((error) => console.error("Error:", error));

  return responseData;
};

/*
  for graphs and output
*/

//to print MAE
const MAE = (responseData) => {
  // Extract the MAE
  var labels = responseData && Object.keys(responseData);

  var MAE = labels.map(function (label) {
    return responseData[label]["MAE"];
  });
  // Get the canvas element
  var ctx = document.getElementById("MAE").getContext("2d");

  // Create a new chart
  var chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "MAE",
          data: MAE,
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
};

//to print MAPE
const MAPE = (responseData) => {
  // Extract the MAPE
  var labels = responseData && Object.keys(responseData);

  var MAPE = labels.map(function (label) {
    return responseData[label]["MAPE"];
  });
  // Get the canvas element
  var ctx = document.getElementById("MAPE").getContext("2d");

  // Create a new chart
  var chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "MAPE",
          data: MAPE,
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
};

//to print MSE
const MSE = (responseData) => {
  // Extract the MSE
  var labels = responseData && Object.keys(responseData);

  var MSE = labels.map(function (label) {
    return responseData[label]["MSE"];
  });
  // Get the canvas element
  var ctx = document.getElementById("MSE").getContext("2d");

  // Create a new chart
  var chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "MSE",
          data: MSE,
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
};

//to print r2score
const r2score = (responseData) => {
  // Extract the r2 scores
  var labels = responseData && Object.keys(responseData);

  var r2Scores = labels.map(function (label) {
    return responseData[label]["r2 score"];
  });
  console.log(r2Scores);
  // Get the canvas element
  var ctx = document.getElementById("R2Score").getContext("2d");

  // Create a new chart
  var chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "R2 Score",
          data: r2Scores,
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
};
