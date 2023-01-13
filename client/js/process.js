document.getElementById("start").addEventListener("click", () => {
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
  process(data)
});

const process = async(data)=>{
    await fetch("http://localhost:5000/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    },
    mode : 'cors',
    body: JSON.stringify(data),
  })
  .then(res => res.json())
  .then(response => {
      console.log(JSON.stringify(response))
  })
  .catch(error => console.error('Error:', error));
}
