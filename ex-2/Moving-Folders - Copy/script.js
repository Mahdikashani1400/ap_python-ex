let folders = ["AP", "SUT", "IE", "DA", "DS", "BP"];
//your code here

const $ = document
let foldersContainer = $.getElementById("folders-container")
let errorContainer = $.getElementById("error-container")

let inputsContainer = $.getElementById("inputs-container")
let itemInput = $.getElementById("item-input")
let countInput = $.getElementById("count-input")
let typeContainer = $.getElementById("type-container")
let upRadio = $.getElementById("UP")
let downRadio = $.getElementById("DOWN")
let submitBtn = $.getElementById("submit-btn")

let radioState = 'up'

function insertFolder(folders) {
    foldersContainer.innerHTML = `
${folders.map(folder => {
        return `<span>${folder}</span>`
    }).join('')}
`
}
insertFolder(folders)

function insertErorr(message) {
    errorContainer.innerHTML = `<p id="error">${message}</p>`
}

let currentIndex = null
let folderTarget = null
let textFolders = null
function submitBtnHandler(e) {
    // e.preventDefault()
    if (!itemInput.value.trim() || !countInput.value.trim()) {
        insertErorr("inputs are invalid!")
    } else if (!folders.includes(itemInput.value)) {
        insertErorr("the folder does not exist!")

    } else {
        currentIndex = folders.findIndex(folder => folder === itemInput.value)
        if (+countInput.value) {
            if (radioState === 'up') {
                if (+currentIndex + Number(countInput.value) >= folders.length) {
                    insertErorr("It's not possible to move anywhere!")
                } else {
                    folderTarget = folders[+currentIndex + Number(countInput.value)]
                    textFolders = folders.join(',')
                    textFolders = textFolders.replace(`${itemInput.value},`, '')
                    textFolders = +currentIndex + Number(countInput.value) !== 1 ? textFolders.replace(`,${folderTarget}`, `,${folderTarget},${itemInput.value}`) : textFolders.replace(`${folderTarget},`, `${folderTarget},${itemInput.value},`)
                    folders = textFolders.split(",")
                    errorContainer.innerHTML = ''
                    insertFolder(folders)
                }
            }
            else {
                if (currentIndex - Number(countInput.value) < 0) {
                    insertErorr("It's not possible to move anywhere!")
                } else {
                    console.log('sf');
                    folderTarget = folders[+currentIndex - Number(countInput.value)]
                    console.log(folderTarget);
                    textFolders = folders.join(',')
                    textFolders = textFolders.replace(`,${itemInput.value}`, '')
                    textFolders = +currentIndex - Number(countInput.value) != folders.length - 2 ? textFolders.replace(`${folderTarget},`, `${itemInput.value},${folderTarget},`) : textFolders.replace(`,${folderTarget}`, `,${itemInput.value},${folderTarget}`)
                    folders = textFolders.split(",")
                    errorContainer.innerHTML = ''

                    insertFolder(folders)
                }
            }
        }
    }
}

upRadio.addEventListener('change', () => {
    radioState = 'up'
})
downRadio.addEventListener('change', () => {
    radioState = 'down'
})

submitBtn.addEventListener('click', submitBtnHandler)
