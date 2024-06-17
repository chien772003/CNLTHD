// Home.js
import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';

const Home = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Home Screen</Text>
      <Button
        title="Go to Categories"
        onPress={() => navigation.navigate('Categories')}
      />
      <Button
        title="Go to Courses"
        onPress={() => navigation.navigate('Courses')}
      />
      <Button
        title="Go to Curriculum"
        onPress={() => navigation.navigate('Curriculum')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
});

export default Home;
