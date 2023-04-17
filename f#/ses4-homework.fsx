// ex 4.1

type PclShape =
    | Rectangle of float * float
    | RightTriangle of float * float

let rect = Rectangle (2.0, 3.0)
let tri = RightTriangle (4.0, 5.0)

let pclArea shape =
    match shape with
    | Rectangle (w, h) -> w * h
    | RightTriangle (b, h) -> b * h / 2.0

let pclPerimeter shape =
    match shape with
    | Rectangle (w, h) -> 2.0 * (w + h)
    | RightTriangle _ -> failwith "Right triangles do not have a perimeter"

type RectangleRecord = {wi : float; len : float}
type RightTriangleRecord = {tbase : float; length : float}

type PclShapeRecord = 
    | RR of RectangleRecord
    | RTR of RightTriangleRecord


(* let rectR = RectangleRecord { wi = 2.0; len = 3.0 }
let triR = RightTriangleRecord { tbase = 4.0; height = 5.0 } *)


