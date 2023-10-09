
// fetch char_width_in_px
let context = document.createElement("canvas").getContext("2d");
context.font = "monospace";
const char_width_in_px = context.measureText("0").width;


  
$(document).ready(ParsonsGlobal.setup);
