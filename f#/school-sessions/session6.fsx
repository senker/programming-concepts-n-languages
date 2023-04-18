open System

let needSome1 = "Coffee" // immutable value
let mutable needSome = "Coffee" // mutable value

printfn "Here comes your %s" needSome

needSome <- "Tea"

// difference between list and array is that list is immutable and array is mutable

let x = [|0|]

x.[0] <- 3

let y = x

let mutable planets =
    [
        "Mercury"; "Venus"; "Earth"
    ]

// prints anything besides "Earth"
planets <- planets |> List.filter (fun p-> p <> "Earth")

printfn "Planets %A" planets

type MutableCar = { Make : string; Model : string; mutable Miles : int}
let driveForASeason car =
    let rng = new Random()
    car.Miles <- car.Miles + rng.Next() % 10000

let tesla = { Make = "Tesla"; Model = "Model X"; Miles = 0}
let bmw = {Make = "BMW"; Model = "i4"; Miles = 50000}

driveForASeason(tesla)
printf "%A" tesla

let a = [|1; 3; 5|]
a.[1] <- 7 + a[1]
printfn "%A" a

let isPrimeNumber x = 
    let mutable i = 2
    let mutable isFactorFound = false
    while not isFactorFound && i < x do
        if x % i = 0 then
            isFactorFound <- true
        i <- i + 1
    not isFactorFound

let intArray = [| for i in 10000000 .. 10004000 -> i |]


let stopWatch = new System.Diagnostics.Stopwatch()
let ResetStopWatch() = stopWatch.Reset(); stopWatch.Start()
let ShowTime() = printfn "It took %d ms " stopWatch.ElapsedMilliseconds

ResetStopWatch()
let primeDetails1 =
    intArray
    |> Array.map (fun x -> (x, isPrimeNumber x))
ShowTime()

ResetStopWatch()
let primeDetails2 =
    intArray
    |> Array.map (fun x -> async { return  (x, isPrimeNumber x)})
    |> Async.Parallel
    |> Async.RunSynchronously
ShowTime()

ResetStopWatch()
let primeDetails3 =
    intArray
    |> Array.Parallel.map (fun x -> (x, isPrimeNumber x))
ShowTime()

// Parallel, Concurrent, Asynchronous -> combined in f# concurrent programming

let printAgent = 
    MailboxProcessor.Start (fun inbox -> 
        // a function to process the message
        let rec msgLoop = async {
            // read a message
            let! msg = inbox.Receive()
            // process a message
            printfn "message is: %s" msg
            // loop to the top
            return! msgLoop // exlamation mark means return immediately
        }
        // start the loop
        msgLoop)


printAgent.Post("testing")
// output is "message is: testing"

let caseConverterActor = 
    MailboxProcessor.Start(fun inbox -> 
        let rec processMessage state = 
            async {
                let! msg = inbox.Receive()
                printfn "received %A" msg
                let newState = "[" + msg + "]"
                printfn "processed %s " (newState.ToUpper())
                return! processMessage newState
            }
        processMessage "initialState"
    )

let slst = ["cat"; "bird"; "fish"; "tarakan"; "sosisca"; "pink"; "bleck"]

//testing of the above
slst |> List.map caseConverterActor.Post

type ``Product agent methods`` = 
    | AddProduct of name : string * origin : string * qty : int
    | GetProduct of AsyncReplyChannel<(string * string * int) list>  

let productMsgQueue = 
    MailboxProcessor<``Product agent methods``>.Start(fun msgHandler -> 
        let rec readProcessMessage products = 
            async {
                let! result = msgHandler.Receive()
                match result with
                | AddProduct(n,o,q) -> 
                    return! readProcessMessage ((n,o,q) :: products)
                | GetProduct(response) -> 
                    let pl = products
                    response.Reply(pl)
                    return! readProcessMessage products
            }
        readProcessMessage []
    )

let addProduct = AddProduct >> productMsgQueue.Post
("Capuccino", "Italy", 35) |> addProduct
("Pink Lady", "Spain", 30) |> addProduct

let resp = productMsgQueue.PostAndReply(GetProduct)
