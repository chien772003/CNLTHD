const Reducer = (currenState, action)=>{
    switch (action.type){
        case "login":
            return action.payload;
        case "logout":
            return null;
    }
}

export default Reducer;