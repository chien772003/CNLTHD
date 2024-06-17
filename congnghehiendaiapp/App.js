import React, { useReducer } from 'react';
import { StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import Categories from './components/Categories/Categories';
import Login from './components/Login/Login';
import Home from './components/Home/Home';
import Courses from './components/Courses/Courses';
import Curriculum from './components/Curriculum/Curriculum';
import Logout from './components/Login/Logout';

import Reducer from './configs/Reducer';
import MyContext from './configs/MyContext';
import Register from './components/Login/RegisterGV';
import RegisterGV from './components/Login/RegisterGV';

const Drawer = createDrawerNavigator();
const Tab = createBottomTabNavigator();

const TabNavigator = () => (
  <Tab.Navigator>
    <Tab.Screen name="Home" component={Home} />
    <Tab.Screen name="Categories" component={Categories} />
    <Tab.Screen name="Courses" component={Courses} />
    <Tab.Screen name="Curriculum" component={Curriculum} />
  </Tab.Navigator>
);

const App = () => {
  const [user, dispatch] = useReducer(Reducer, null);

  return (
    <MyContext.Provider value={[user, dispatch]}>
      <NavigationContainer>
        <Drawer.Navigator screenOptions={({ navigation }) => ({
          headerRight: user ? () => <Logout navigation={navigation} dispatch={dispatch} /> : null,
        })}>
          {user === null ? (
            <Drawer.Screen name="Register" component={RegisterGV} />
          ) : (
            <Drawer.Screen name="App" component={TabNavigator} />
          )}
        </Drawer.Navigator>
      </NavigationContainer>
    </MyContext.Provider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});

export default App;
