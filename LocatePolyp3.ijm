run("Make Binary", "method=Default background=Default calculate");
setOption("BlackBackground", false);
run("Dilate", "stack");
run("Dilate", "stack");
run("Fast Filters", "link filter=[background from maxima] x=10 y=10 preprocessing=none offset=128 stack");
run("Make Binary", "method=Default background=Dark calculate");
