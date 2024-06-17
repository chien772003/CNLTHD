import React, { useEffect, useState } from "react";
import { ActivityIndicator, View, Text, StyleSheet, TouchableOpacity, Alert } from "react-native";
import MyStyles from "../../styles/MyStyles";
import API, { endpoints } from "../../configs/API";
import styles from "./Styles"
import Courses from "../Courses/Courses";

const Categories = () => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadCategories = async () => {
            try {
                let allCategories = [];
                let nextUrl = endpoints['categories'];

                while (nextUrl) {
                    let res = await API.get(nextUrl);
                    allCategories = [...allCategories, ...res.data.results];
                    nextUrl = res.data.next;
                }

                setCategories(allCategories);
            } catch (ex) {
                console.error("Error loading categories:", ex);
                Alert.alert("Error", `Network Error: ${ex.message}`);
            } finally {
                setLoading(false);
            }
        };
        loadCategories();
    }, []);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Categories</Text>
            
            {loading ? <ActivityIndicator /> : (
                <>
                    {categories && categories.length > 0 ? (
                        categories.map(cat => (
                            <TouchableOpacity key={cat.id} style={styles.categoryContainer}>
                                <Text style={styles.categoryText}>{cat.name}</Text>
                            </TouchableOpacity>
                        ))
                    ) : (
                        <Text>No categories available</Text>
                    )}
                </>
            )}
        </View>
    );
};

export default Categories;