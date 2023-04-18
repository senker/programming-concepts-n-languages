open System.IO

let studentName = fst ("Name", 123456)
let studentName2 = ("Sasamba", 69420) |> fst

// get the length of a square
let square x = x * x
let toString (x:int) = x.ToString()
let stringLen (x:string) = x.Length
let lenOfSquare = square >> toString >> stringLen
//toString it;; // it refers to the last value

let (<|) f x = f x
List.iter (printfn "%d") [1 .. 3]
List.iter (printfn "%d") <| [1 .. 3]

let negate x = -x

(square >> negate) 10
(square << negate) 10

[[1]; []; [4;5;6]; [3;4]; []; []; []; [9]] |> List.filter (not << List.isEmpty)



type PclShape =
    | Rectangle of w: float * h: float
    | RightTriangle of float * float

(* let myRectangle = Rectangle (5.0, 7.0)
let myTriangle = RightTriangle (8.0, 6.0) *)

let pclArea shape =
    match shape with
    | Rectangle (w, h) -> w * h
    | RightTriangle (bs, h) -> bs * h * 0.5

type RectangleRecord = {wi : float; len : float}
type RightTriangleRecord = {tbase : float; length : float}

type PclShapeRecord = 
    | RR of RectangleRecord
    | RTR of RightTriangleRecord

type CoffeeGrainType = 
    | Arabica
    | Robusta

type CoffeR = {graintype : CoffeeGrainType; size : int}

let c1 = {graintype = CoffeeGrainType.Arabica; size = 2}

type Size = Large | Medium
type CoffeeType = Americano | Latte 

type CoffeeRecord = {ctype : CoffeeType; size : Size}