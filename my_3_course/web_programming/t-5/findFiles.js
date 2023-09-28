const fs = require('fs');
const path = require('path');

// текущая директория
const currentDirectory = process.cwd();

// фильтрация по шаблону
function filterFilesByPattern(pattern) {
  const files = fs.readdirSync(currentDirectory);

  const filteredFiles = files.filter((file) => {
    const regex = new RegExp(pattern.replace(/\*/g, '.*').replace(/\?/g, '.'));
    return regex.test(file);
  });

  return filteredFiles;
}

const searchPattern = process.argv[2];

if (!searchPattern) {
  console.log('Пожалуйста, укажите шаблон для поиска файлов.');
  process.exit(1);
}

console.log(`Ищем файлы, удовлетворяющие шаблону: ${searchPattern}`);
const matchingFiles = filterFilesByPattern(searchPattern);

if (matchingFiles.length === 0) {
  console.log('Файлы не найдены.');
} else {
  console.log('Совпадающие файлы:');
  matchingFiles.forEach((file) => {
    console.log(file);
  });
}
