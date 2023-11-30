// Motel Customer Object
const MotelCustomer = {
    name: "John Doe",
    birthDate: "1990-05-15",
    gender: "Male",
    roomPreferences: ["Non-smoking", "King-sized bed"],
    paymentMethod: "Credit Card",
    mailingAddress: {
      street: "123 Main St",
      city: "Anytown",
      state: "CA",
      zipCode: "12345",
    },
    phoneNumber: "555-123-4567",
    checkInDate: "2023-11-01",
    checkOutDate: "2023-11-05",
  
    // Method to calculate age of the customer
    calculateAge: function () {
      const today = new Date();
      const birthDate = new Date(this.birthDate);
      let age = today.getFullYear() - birthDate.getFullYear();
      const monthDiff = today.getMonth() - birthDate.getMonth();
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
      return age;
    },
  
    // Method to calculate duration of stay
    calculateStayDuration: function () {
      const checkIn = new Date(this.checkInDate);
      const checkOut = new Date(this.checkOutDate);
      const duration = (checkOut - checkIn) / (1000 * 60 * 60 * 24); // in days
      return duration;
    },
  
    // Method to generate a description of the customer
    generateDescription: function () {
      const age = this.calculateAge();
      const stayDuration = this.calculateStayDuration();
      return `
        Name: ${this.name}
        Age: ${age}
        Gender: ${this.gender}
        Room Preferences: ${this.roomPreferences.join(", ")}
        Payment Method: ${this.paymentMethod}
        Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state} ${this.mailingAddress.zipCode}
        Phone Number: ${this.phoneNumber}
        Check-in Date: ${this.checkInDate}
        Check-out Date: ${this.checkOutDate}
        Duration of Stay: ${stayDuration} days
      `;
    },
  };
  
  // Generate the description of the customer
  const customerDescription = MotelCustomer.generateDescription();
  console.log(customerDescription); // Output the description to the console
  