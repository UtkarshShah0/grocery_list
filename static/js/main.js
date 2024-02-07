function check_me(input_id) {
  const checked_input = document.querySelector("input[id=" + input_id + "]");
  const checked_label = document.querySelector("label[name=" + input_id + "]");

  if (checked_input.checked) {
    checked_label.style.textDecoration = "line-through";
  } else {
    checked_label.style.textDecoration = "";
  }

  const btn = document.getElementById("remove_btn");
  btn.style.color = "#FFF";
  btn.style.backgroundColor = "#FE7575";
  btn.style.cursor = "pointer";
}
