from graphviz import Source
temp = """
digraph { 

  node [shape=circle,fontsize=8,fixedsize=true,width=0.9]; 
  edge [fontsize=8]; 
  rankdir=LR;

  "low-priority" [shape="doublecircle" color="orange"];
  "high-priority" [shape="doublecircle" color="orange"];

  "s1" -> "low-priority";
  "s2" -> "low-priority";
  "s3" -> "low-priority";

  "low-priority" -> "s4";
  "low-priority" -> "s5";
  "low-priority" -> "high-priority" [label="wait-time exceeded"];

  "high-priority" -> "s4";
  "high-priority" -> "s5";

}
"""
Source(temp).view()
