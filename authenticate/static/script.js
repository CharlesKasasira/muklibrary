const message = document.getElementById("msg");

setTimeout(() => {
  message.remove();
}, 1500);

const borrowBook = () => {
  console.log("Book borrowed successfully");
};
