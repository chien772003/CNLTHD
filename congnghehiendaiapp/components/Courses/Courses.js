import React, { useEffect, useState } from "react";
import { ActivityIndicator, View, Text, StyleSheet, Alert,TouchableOpacity } from "react-native";
import MyStyles from "../../styles/MyStyles";
import API, { endpoints } from "../../configs/API";
import styles from "./Styles"

const Coures = () => {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadCourses = async () => {
            try {
                let res = await API.get(endpoints['courses']);
                // console.log("API response:", res.data.results); //console ra thử
                setCourses(res.data.results);
            } catch (ex) {
                console.error("Error loading courses:", ex);
                Alert.alert("Error", `Network Error: ${ex.message}`);
            } finally {
                setLoading(false);
            }
        };
        loadCourses();
    }, []);

    return (
        <View style={styles.margin}>
            <Text style={styles.subject}>Các Môn Học</Text>
            
            {loading ? <ActivityIndicator /> : (
                <>
                    {courses && courses.length > 0 ? (
                        courses.map(c => (
                            <View key={c.id} style={styles.courseContainer}>
                                <Text style={styles.courseText}>{c.name}</Text>
                            </View>
                        ))
                    ) : (
                        <Text>Không có khóa học nào</Text>
                    )}
                </>
            )}
        </View>
    );
};

export default Coures;
