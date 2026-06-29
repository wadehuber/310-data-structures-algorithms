{ Simple Graph Data Structure  (CSC310 Module 6B - Graphs)
  ========================================================

  Adjacency-list representation using dynamic arrays: the graph holds an ordered
  array of vertices, and each vertex holds a dynamic array of (dest, weight)
  edges.  An undirected edge is stored as two directed edges.

  Build & run (Free Pascal):  fpc graph.pas && ./graph }

program GraphDemo;

{$mode objfpc}{$H+}

type
  TEdge = record
    dest: string;
    weight: integer;
  end;
  TEdgeArray = array of TEdge;
  TVertex = record
    name: string;
    edges: TEdgeArray;
  end;
  TGraph = record
    verts: array of TVertex;
  end;

function FindVertex(var g: TGraph; const name: string): integer;
var i: integer;
begin
  for i := 0 to High(g.verts) do
    if g.verts[i].name = name then exit(i);
  FindVertex := -1;
end;

procedure AddVertex(var g: TGraph; const name: string);
var n: integer;
begin
  if FindVertex(g, name) <> -1 then exit;
  n := Length(g.verts);
  SetLength(g.verts, n + 1);
  g.verts[n].name := name;
  SetLength(g.verts[n].edges, 0);
end;

procedure AddDirected(var g: TGraph; const u, v: string; w: integer);
var i, m: integer;
begin
  i := FindVertex(g, u);
  m := Length(g.verts[i].edges);
  SetLength(g.verts[i].edges, m + 1);
  g.verts[i].edges[m].dest := v;
  g.verts[i].edges[m].weight := w;
end;

procedure AddEdge(var g: TGraph; const u, v: string; w: integer; directed: boolean);
begin
  AddVertex(g, u);
  AddVertex(g, v);
  AddDirected(g, u, v, w);
  if not directed then AddDirected(g, v, u, w);
end;

{ Return a copy of vertex V's edges, sorted by destination name. }
function SortedEdges(var g: TGraph; const v: string): TEdgeArray;
var i, j, idx: integer; tmp: TEdge; e: TEdgeArray;
begin
  idx := FindVertex(g, v);
  e := Copy(g.verts[idx].edges, 0, Length(g.verts[idx].edges));
  for i := 0 to High(e) - 1 do            { simple insertion-ish bubble sort }
    for j := 0 to High(e) - 1 - i do
      if e[j].dest > e[j+1].dest then
      begin
        tmp := e[j]; e[j] := e[j+1]; e[j+1] := tmp;
      end;
  SortedEdges := e;
end;

function EdgeWeight(var g: TGraph; const u, v: string): integer;
var i, idx: integer;
begin
  idx := FindVertex(g, u);
  for i := 0 to High(g.verts[idx].edges) do
    if g.verts[idx].edges[i].dest = v then exit(g.verts[idx].edges[i].weight);
  EdgeWeight := -1;
end;

procedure PrintGraph(var g: TGraph);
var i, j: integer; e: TEdgeArray;
begin
  writeln('Graph (undirected, weighted) - adjacency list:');
  for i := 0 to High(g.verts) do
  begin
    write('  ', g.verts[i].name, ' -> ');
    e := SortedEdges(g, g.verts[i].name);
    for j := 0 to High(e) do
    begin
      write(e[j].dest, '(', e[j].weight, ')');
      if j < High(e) then write(', ');
    end;
    writeln;
  end;
end;

var
  g: TGraph;
  e: TEdgeArray;
  j: integer;
begin
  SetLength(g.verts, 0);
  { A small Arizona road network (miles).  Not an assignment graph. }
  AddVertex(g, 'PHX');
  AddVertex(g, 'TUS');
  AddVertex(g, 'MESA');
  AddVertex(g, 'TEMPE');
  AddEdge(g, 'PHX',  'MESA',  20,  false);
  AddEdge(g, 'PHX',  'TEMPE', 11,  false);
  AddEdge(g, 'MESA', 'TEMPE', 8,   false);
  AddEdge(g, 'PHX',  'TUS',   116, false);
  AddEdge(g, 'TUS',  'MESA',  100, false);

  PrintGraph(g);

  write('Neighbors of PHX: ');
  e := SortedEdges(g, 'PHX');
  for j := 0 to High(e) do
  begin
    write(e[j].dest);
    if j < High(e) then write(', ');
  end;
  writeln;
  writeln('Weight PHX-MESA: ', EdgeWeight(g, 'PHX', 'MESA'));
end.
