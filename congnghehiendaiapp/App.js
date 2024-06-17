import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Home from './components/Courses/Courses';
import MyStyles from './styles/MyStyles';
import Courses from './components/Courses/Courses';
import Categories from './components/Categories/Categories';
import Login from './components/Login/Login';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  return (
    <NavigationContainer>
      {isLoggedIn ? (
        <Drawer.Navigator initialRouteName="Home">
          <Drawer.Screen name="Home" component={Home} />
          <Drawer.Screen name="Categories" component={Categories} />
          <Drawer.Screen name="Courses" component={Courses} />
          <Drawer.Screen name="Curriculum" component={Curriculum} />
          {/* Để implement phần Account và logout, bạn có thể thêm Screen mới hoặc chỉnh sửa màn hình Account */}
        </Drawer.Navigator>
      ) : (
        <Stack.Navigator>
          <Stack.Screen
            name="Login"
            component={Login}
            options={{ headerShown: false }} // Ẩn header trong màn hình Login
            initialParams={{ handleLogin }} // Truyền hàm handleLogin cho màn hình Login
          />
        </Stack.Navigator>
      )}
    </NavigationContainer>
  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
