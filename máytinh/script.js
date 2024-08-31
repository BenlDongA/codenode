// Khởi tạo các biến
let currentInput = '0';  // Lưu trữ số hiện tại mà người dùng đang nhập
let previousInput = '';  // Lưu trữ số trước đó
let operator = null;     // Lưu trữ toán tử hiện tại
let resultDisplayed = false;  // Cờ để xác định xem kết quả cuối cùng có đang hiển thị không

// Lấy phần tử hiển thị
const resultDisplay = document.getElementById('result');
// Lấy tất cả các nút số và toán tử
const numberButtons = document.querySelectorAll('.number');
const operatorButtons = document.querySelectorAll('.operator');
const clearButton = document.querySelector('.clear');
const equalsButton = document.querySelector('.equals');

// Gán sự kiện cho các nút số
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        handleNumber(button.textContent); // Gọi hàm handleNumber với số tương ứng trên nút
    });
});

// Gán sự kiện cho các nút toán tử
operatorButtons.forEach(button => {
    button.addEventListener('click', () => {
        handleOperator(button.textContent); // Gọi hàm handleOperator với toán tử tương ứng trên nút
    });
});

// Gán sự kiện cho nút xóa (Clear)
clearButton.addEventListener('click', () => {
    clear();  // Gọi hàm clear() để xóa dữ liệu
});

// Gán sự kiện cho nút "="
equalsButton.addEventListener('click', () => {
    calculate();  // Gọi hàm calculate() để thực hiện phép toán
});

// Hàm xử lý số khi người dùng nhấn
function handleNumber(number) {
    if (resultDisplayed) {
        // Nếu kết quả đã được hiển thị, làm mới với số mới
        currentInput = number;
        resultDisplayed = false;
    } else {
        // Thêm số vào chuỗi hiện tại
        currentInput = currentInput === '0' ? number : currentInput + number;
    }
    updateDisplay(); // Cập nhật màn hình hiển thị
}

// Hàm xử lý toán tử khi người dùng nhấn
function handleOperator(op) {
    if (currentInput === '' && op === '-') {
        // Nếu không có số hiện tại và toán tử là '-', cho phép nhập số âm
        currentInput = '-';
        updateDisplay();
        return;
    }

    if (operator !== null) {
        // Nếu đã có một toán tử trước đó, thực hiện phép toán trước khi thay đổi toán tử
        calculate();
    }

    // Lưu trữ số hiện tại và toán tử
    previousInput = currentInput;
    operator = op;
    currentInput = '';
    resultDisplayed = false;
    updateDisplay();
}

// Hàm tính toán kết quả
function calculate() {
    let result;
    const prev = parseFloat(previousInput);
    const current = parseFloat(currentInput);

    if (isNaN(prev) || isNaN(current)) return;

    switch (operator) {
        case '+':
            result = prev + current;
            break;
        case '-':
            result = prev - current;
            break;
        case '*':
            result = prev * current;
            break;
        case '/':
            if (current === 0) {
                alert("Không thể chia cho 0");
                clear();
                return;
            }
            result = prev / current;
            break;
        default:
            return;
    }

    currentInput = result.toString();
    operator = null;
    previousInput = '';
    resultDisplayed = true;
    updateDisplay();
}
// Hàm cập nhật màn hình hiển thị
function updateDisplay() {
    if (operator) {
        // Nếu có toán tử, hiển thị số trước và toán tử cùng với số hiện tại
        resultDisplay.value = `${previousInput} ${operator} ${currentInput}`;
    } else {
        // Nếu không có toán tử, chỉ hiển thị số hiện tại
        resultDisplay.value = currentInput;
    }
}
// Hàm xóa dữ liệu và đặt lại máy tính
function clear() {
    currentInput = '0';  // Đặt lại giá trị hiện tại về '0'
    previousInput = '';  // Xóa giá trị trước đó
    operator = null;     // Đặt lại phép toán
    resultDisplayed = false;  // Đặt lại cờ kết quả hiển thị
    updateDisplay();  // Cập nhật lại màn hình hiển thị
}
