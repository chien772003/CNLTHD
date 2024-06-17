import { useContext } from "react";
import { Button } from "react-native"
import MyContext from "../../configs/MyContext";

const Logout =({navigation})=>{
    const [user,dispatch]=useContext(MyContext);
    const logout =()=>{
        dispatch({
            "type":"logout"
        })
    }
    if(user === null)
        <Button title="Login"onPress={()=>navigator.navigate("Login")}/>
    return(
        

        <Button title="Logout"onPress={logout}/>
    )
}
export default Logout;