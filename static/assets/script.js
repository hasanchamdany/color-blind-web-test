let inputData = [];
// console.log("test")
const btn = document.getElementById("generate");
const disease = document.getElementById("diseaseType");

// for (var i = 0; i < 10; i++){
//     inputData.push.getElementById(i).value
// }

btn.onclick = function () {
  const form = document.getElementById("form");
  // console.log(form["0"])
  // console.log(form["0"].value)
  for (var i = 0; i < 10; i++) {
    inputData[i] = form[i].value;
  }
  // console.log(inputData[0])
  fetch("/test", {
    method: "POST",
    body: JSON.stringify({
      answers: inputData,
    }),
  })
    .then((result) => result.json())
    .then((result) => {
      res = result.result;
      console.log(res);
      if (res.length === 0) {
        disease.innerHTML = `<p>Your disease is not detected, please fill all of the answers</p>`;
        return;
      }
      disease.innerHTML = `You are ${res}`;
    });
};
