export const trainingPercetages = [50, 55, 60, 65, 70, 75, 80, 85, 90];

export const trainingValidation = (start, end, option) => {
  if (start <= end && Number(option) >= 50 && Number(option) <= 90) {
    return true;
  }

  return false;
};
