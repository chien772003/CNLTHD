import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const RegisterGV = () => {
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [birthYear, setBirthYear] = useState('');
  const [email, setEmail] = useState('');
  const [hocVi, setHocVi] = useState('');
  const [password, setPassword] = useState('');
  const [avatar, setAvatar] = useState(null);

  // Mặc định đăng ký là Giảng viên
  const isTeacher = true;
  const isStudent = false;

  const pickImage = async () => {
    try {
      let { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
      if (status !== 'granted') {
        alert("Quyền truy cập bị từ chối!");
        return;
      }
      
      let result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.Images,
        allowsEditing: true,
        aspect: [4, 3],
        quality: 1,
      });

      if (!result.cancelled) {
        setAvatar(result.uri);
        console.log("Avatar URI:", result.uri);
      } else {
        console.log("Image picking cancelled");
      }
    } catch (error) {
      console.log("Error picking image:", error.message);
    }
  };

  const handleRegister = async () => {
    try {
      // Validate input fields (e.g., username, email, password, ...)
      // Save account information and avatar URI to backend server
      const formData = {
        username,
        firstName,
        lastName,
        birthYear,
        isTeacher,
        isStudent,
        email,
        hocVi,
        password,
        avatar
      };

      // Example: Send registration data to backend API
      const response = await fetch('https://http://10.17.20.6:8000/users/register-teacher', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }

      // Handle success (e.g., show confirmation message, navigate to login screen)
      console.log('Registration successful');
      // Example: Navigate to login screen
      // navigation.navigate('Login');
    } catch (error) {
      console.error('Error registering:', error);
      // Handle error (e.g., show error message to user)
      alert('Đăng ký không thành công. Vui lòng thử lại sau.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.subject}>Đăng ký Tài Khoản Giảng Viên</Text>
      <TextInput
        placeholder='Tên đăng nhập...'
        style={styles.input}
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        placeholder='Họ...'
        style={styles.input}
        value={firstName}
        onChangeText={setFirstName}
      />
      <TextInput
        placeholder='Tên...'
        style={styles.input}
        value={lastName}
        onChangeText={setLastName}
      />
      <TextInput
        placeholder='Năm sinh...'
        style={styles.input}
        value={birthYear}
        onChangeText={setBirthYear}
        keyboardType='numeric'
      />
      <TextInput
        placeholder='Email...'
        style={styles.input}
        value={email}
        onChangeText={setEmail}
        keyboardType='email-address'
      />
      <TextInput
        placeholder='Học vị...'
        style={styles.input}
        value={hocVi}
        onChangeText={setHocVi}
      />
      <TouchableOpacity style={styles.imagePicker} onPress={pickImage}>
        {avatar ? (
          <Text style={styles.imagePickerText}>Đã chọn ảnh</Text>
        ) : (
          <Text style={styles.imagePickerText}>Chọn ảnh đại diện</Text>
        )}
      </TouchableOpacity>
      <TextInput
        placeholder='Nhập mật khẩu...'
        style={styles.input}
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <TouchableOpacity style={styles.button} onPress={handleRegister}>
        <Text style={styles.buttonText}>Đăng ký</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20
  },
  subject: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20
  },
  input: {
    height: 40,
    borderColor: '#ccc',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10
  },
  button: {
    backgroundColor: '#007BFF',
    borderRadius: 5,
    padding: 10,
    marginTop: 10
  },
  buttonText: {
    color: 'white',
    textAlign: 'center'
  },
  imagePicker: {
    height: 40,
    borderColor: '#ccc',
    borderWidth: 1,
    marginBottom: 10,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 10
  },
  imagePickerText: {
    textAlign: 'center'
  }
});

export default RegisterGV;
