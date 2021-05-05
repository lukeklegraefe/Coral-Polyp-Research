run("Make Binary", "method=Default background=Default calculate");
setOption("BlackBackground", false);
run("Dilate", "stack");
run("Dilate", "stack");
run("Fast Filters", "link filter=[background from maxima] x=6 y=6 preprocessing=none offset=128 stack");
run("Make Binary", "method=Default background=Light calculate");
