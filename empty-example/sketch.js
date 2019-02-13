var slider;
var Opts = ["heads", "tails"];
// var ht = random(Opts);
function setup() {
  createCanvas(windowWidth, windowHeight);
  textSize(17);
  //textColor(100);
  sliderAng = createSlider(0, PI, PI/4, .001); // angle of branches
  sliderAng.position(windowWidth*4/5,220);
  sliderRep = createSlider(0, 7, 5, 1); // how many times the branch repeats its self
  sliderRep.position(windowWidth*4/5,300);
  sliderAngCh = createSlider(.25, 8, .9, .01); //Angle Disruption
  sliderAngCh.position(windowWidth*4/5,380);
  sliderLenCh = createSlider(0, 1, .67, .1); // rate of branch length change
  sliderLenCh.position(windowWidth*4/5,460);
  sliderTBranchLen = createSlider(0, 300, 246, 1); // total length of beginning branch
  sliderTBranchLen.position(windowWidth*4/5,540);

  // TBranchLen = sliderTBranchLen.value();
  // sliderRandom = createSlider(0, TBranchLen, 0, 1);
  // sliderRandom.position(displayWidth*4/5,620);
  // noLoop();
}
function draw() {
  background(51);
  angle = sliderAng.value();
  rep = sliderRep.value();
  AngChange = sliderAngCh.value();
  LenCh = sliderLenCh.value();
  TBranchLen = sliderTBranchLen.value();
  // RandomNum = sliderRandom.value();
  noStroke();
  fill(300);
  text("Angle of branches", sliderAng.x, sliderAng.y-5);
  text("Branch Repetitions", sliderRep.x, sliderRep.y-5);
  text("Angle Disruption", sliderAngCh.x, sliderAngCh.y-5);
  text("Branch Length", sliderLenCh.x, sliderLenCh.y-5);
  text("Tree height", sliderTBranchLen.x, sliderTBranchLen.y-5);
  // var Cflips = 0;
  // if(1 > Cflips){
  // }
  // text("Randomization", sliderRandom.x, sliderRandom.y-5);
  stroke(225);
  translate(windowWidth*5/12, height);
  branch(TBranchLen, 0)
}
text(random(Opts), sliderTBranchLen.x, sliderTBranchLen.y+100);

function branch(len, crep) {

  line(0, 0, 0, -len);
  translate(0, -len);
  //while(i << 10){
  if(rep > crep) {
    push();
    rotate(angle * AngChange);
    branch(len * LenCh, crep+1);
    pop();
    push();
    rotate(-angle * AngChange);
    branch(len * LenCh, crep+1);
    pop();
    push();
    rotate(angle * 1/AngChange);
    branch(len * LenCh*.5, crep+1);
    pop();
    push();
    rotate(-angle* 1/AngChange);
    branch(len * LenCh*.5, crep+1);
    pop();

  //    }
    }
}
// function windowResized() {
//   setup();
// }

// while mouseDragged(){
//   redraw();
// }
