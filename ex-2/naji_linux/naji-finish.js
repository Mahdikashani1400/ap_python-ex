// var array = [
//     // [3, 3],
//     ["B", "B", "P", "P", "P", "P"],
//     ["P", "P", "M", "B", "B", "B"],
//     ["P", "P", "B", "B", "B", "B"],
//     ["B", "B", "B", "B", "B", "B"],
// ]
// ]
// var array = [
//     // [3, 3],
//     ["B", "B", "P", "P", "P", "P"],
//     ["P", "P", "M", "B", "P", "P"],
//     ["P", "P", "B", "P", "P", "P"],
//     ["B", "B", "P", "B", "B", "B"],

// ]
// var array = [
//     // [3, 3],
//     ["B", "B", "P"],
//     ["B", "M", "B"],
//     ["P", "B", "P"],

// ]

// مرحله بعد اینه که هر جا رسید به پی اون بیه حذف بشه

// avali tedad satr va dovomi tedad soton

let bArray = []
let bFakeArray = []
let mArray = []
let mPoint = []
let steps = []
let stepState = false
let allSteps = []
let counter = 0;


let nums = readline().split(' ');
let array = []
for (let i = 0; i < nums[0]; i++) {
    let userInput = readline().split('')
    array.push(userInput)

}


function solver() {
    if (!bArray.length) {
        for (let i = 0; i < array.length; i++) {
            for (let j = 0; j < array[i].length; j++) {
                if (array[i][j] == 'M') {
                    mArray = [i + 1, j + 1]
                    mPoint = [i + 1, j + 1]

                } else if (array[i][j] == "B") {
                    bArray.push([i + 1, j + 1])
                }
            }
        }
        bFakeArray = [...bArray]
        solver()
    } else {
        if (mArray[0] == array.length) {
            stepState = true
            steps.push("D")
            allSteps.push([...steps])
            steps.pop()
            if (mArray[1] == 1) {
                steps.push("L")
                allSteps.push([...steps])
                steps.pop()
            }
            if (mArray[1] == array[0].length) {
                steps.push("R")
                allSteps.push(steps)

            }



        } else if (mArray[0] == 1) {
            stepState = true

            steps.push("U")
            allSteps.push([...steps])
            steps.pop()
            if (mArray[1] == 1) {
                steps.push("L")
                allSteps.push([...steps])
                steps.pop()
            }
            if (mArray[1] == array[0].length) {
                steps.push("R")
                allSteps.push([...steps])

            }



        } else if (mArray[1] == 1) {
            steps.push("L")
            allSteps.push([...steps])
            stepState = true

        }
        else if (mArray[1] == array[0].length) {
            steps.push("R")
            allSteps.push([...steps])
            stepState = true

        }
        else {
            counter++
            for (let i = 0; i < bFakeArray.length; i++) {
                const step = bFakeArray[i];


                if (step[0] === mArray[0] + 1 && step[1] === mArray[1] && steps[steps.length - 1] !== 'U') {
                    steps.push("D")
                    mArray = step
                    break

                } else if (step[0] === mArray[0] - 1 && step[1] === mArray[1] && steps[steps.length - 1] !== 'D') {
                    steps.push("U")
                    mArray = step
                    break


                }
                else if (step[1] === mArray[1] + 1 && step[0] === mArray[0] && steps[steps.length - 1] !== 'L') {
                    steps.push("R")
                    mArray = step
                    break


                }
                else if (step[1] === mArray[1] - 1 && step[0] === mArray[0] && steps[steps.length - 1] !== 'R') {
                    steps.push("L")
                    mArray = step
                    break

                } else {
                    // console.log(bFakeArray, steps, mArray);
                    bFakeArray = [...bFakeArray].filter(step => {
                        if (step[0] == mArray[0] && step[1] == mArray[1]) {
                        } else {
                            return step

                        }
                    })
                }
            }

            if (steps.lengt || (counter < array.length * array[0].length)) {
                // counter = 0
                solver()
            }
        }

        if (stepState) {
            stepState = false
            bArray = [...bArray].filter(step => {
                if (step[0] == mArray[0] && step[1] == mArray[1]) {
                } else {
                    return step

                }
            })
            bFakeArray = [...bArray]

            steps = []
            mArray = [...mPoint]
            if (allSteps.length != 4) {
                solver()
            }
        }
    }
}
solver()

if (allSteps.length) {
    // console.log(allSteps);
    let answer = []
    let minSteps = 9999999999
    allSteps.forEach(steps => {
        if (minSteps >= steps.length) {
            minSteps = steps.length
            answer.push(steps)
        }
    })
    answer.forEach(step => {
        console.log(step.join(''));
    })
} else {
    // console.log(steps);
    console.log("there is no escape!");
}

// مینی لینوکس وقتی خارج میشه که تو سطر اول یا سطر اخر یا ستون اول یا ستون اخر باشه.

// وقتی به مقصد رسیدیم، آن مقصد از لیست ارایه ها پاک میشود.