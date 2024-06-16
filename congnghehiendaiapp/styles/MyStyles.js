import { StyleSheet } from "react-native";

const MyStyles = StyleSheet.create({
    container: {
        flex: 1
    }, subject: {
        fontSize: 25,
        fontWeight: "bold",
        color: "blue"
    }, row: {
        flexDirection: "row"
    }, wrap: {
        flexWrap: "wrap"
    },margin: {
        margin: 5
    }, avatar: {
        width: 80,
        height: 80,
        borderRadius: 20
    }, center: {
        alignSelf: "center"
    }
});
export default MyStyles;