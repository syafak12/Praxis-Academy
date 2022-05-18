from ast import pattern


{
  $jsaonchema:{
      bsonType: "object",
      requered:["nis", "nama_depan", "telp", "jenis_kelamin"],
      properties:{
          nis:{
              bsonType:"string",
              pattern:[0-9]{9,}",
              description:"wajib ada dan harus tipe string dengan karakter number sebanyak 9 karakter atau lebih"
          },
          nama_depan:{
              bsonType:"string",
              description:"wajib ada dan harus tipe string"
          },
          nama_belakang:{
              bsonType:"string",
              description:"harus tipe string"
          },
          alamat:{
              bsonType:"string"
              description:"harus tipe string"
          },
          email:{
              bsonType:"string",
              pattern:"^.+/@.+$",
              description:"wajib ada dan harus tipe string dengan email yang valid"
          },
          telp:{
              bsonType:["string"],
              items:{
                  bsonType:"string"
                  pattern"[0-9{11,13}]"
              },
              pattern:"[0-9]{11,13}"
          },
          jenis_kelamin:{
              enum:["p","l"],
              description:"wajib ada dan hanya menerima nilai P ata L"
          }
      }
  }  
}