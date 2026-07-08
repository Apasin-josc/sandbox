//Union = "this can be one of several types," written with |:
let id: number | string;
id = 5
id = "abc"
//id = true;  wrong either it should be a number or string


//Literal types = the type is an exact value, not just "any string":
let difficulty: "easy" | "medium" | "hard";
difficulty = "medium"
//difficulty = "hardcore" <<as difficulty says, it can only be easy,medium or hard>>


function printId(id: number | string){
    if(typeof id === "string"){
        id.toUpperCase();
    }
}

let status: "todo" | "done";
status = "done";
//status = "finished"; error

function describeSet(weight: number | "bodyweight"){
    if(typeof weight === "string"){
        return "BW"
    }

    if(typeof weight === "number"){
        return `${weight}kg`
    }
}