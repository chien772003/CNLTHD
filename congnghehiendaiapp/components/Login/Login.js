import React, { useContext, useState } from 'react';
import { View, Text, TextInput, TouchableOpacity } from 'react-native';
import styles from "./Styles"
import MyStyles from '../../styles/MyStyles';
import MyContext from '../../configs/MyContext';
import API,{ endpoints } from '../../configs/API';

const Login = ({navigation}) => {
  const [username, setUsername] = useState('');
  const [password, setPass] = useState('');
  const [user, dispatch] = useContext(MyContext);

  const login = async () => {
    try {
      let res = await API.post(endpoints['login'],{
        'username':username,
        'password': password,
        'client_id':"vSK5NUNtUOzy5AVaB19zOFPnBkkfwSndV1PNhScb",
        'client_secret': "79DpPlhsDdihacM9s3QmepmDBU6L4UHiqyCGr0b52vudz0mV8mk6lSGYf4pazzll9SCX7hmxa0EzC52ocesvcmlkHE7kpTmpZkwVrAjwf3qvQJeFnfRioLKBn3Srn62a",
        'grant_type':"password"
      });
      console.info(res.data)
    } catch (ex) {
      console.error(ex);
    }
    
  }

  return (
    <View style={styles.container}>
      <Text style={MyStyles.subject}>Login</Text>
      <TextInput 
        value={username} 
        onChangeText={t => setUsername(t)} 
        placeholder='Tên đăng nhập...' 
        style={styles.input} 
      />
      <TextInput 
        value={password} 
        onChangeText={t => setPass(t)} 
        placeholder='Nhập mật khẩu...' 
        style={styles.input} 
        secureTextEntry
      />
      <TouchableOpacity onPress={login}>
        <Text style={styles.button}>Login</Text>
      </TouchableOpacity>
    </View>
  )
};

export default Login;
