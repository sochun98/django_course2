function datetimeToString(datetime) {
    if (datetime === null) {
        return "미완료"
    }
    return new Date(datetime).toLocaleString()
}

function completeOrNot(complete) {
    if (complete === true) {
        return "완료"
    }
    return "진행중"
}