import { StyleSheet } from "react-native";
const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
        backgroundColor: '#fff',
        borderRadius: 5,
        marginBottom: 20,
        elevation: 3,
    },
    subject: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    addCourseContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        marginBottom: 10,
    },
    input: {
        flex: 1,
        height: 40,
        borderWidth: 1,
        borderColor: '#ccc',
        borderRadius: 5,
        paddingHorizontal: 10,
    },
    addButton: {
        marginLeft: 10,
        backgroundColor: '#007bff',
        borderRadius: 5,
        padding: 10,
    },
    addButtonText: {
        color: '#fff',
        fontSize: 20,
        fontWeight: 'bold',
    },
    courseContainer: {
        marginBottom: 10,
        padding: 10,
        backgroundColor: '#f0f0f0',
        borderRadius: 5,
        borderWidth: 1,
        borderColor: '#ccc'
    },
    courseText: {
        fontSize: 18,
    },
});
export default styles;