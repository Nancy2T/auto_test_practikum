SELECT
  "Couriers".login,
  COUNT(*)
FROM "Orders" 
JOIN "Couriers" ON "Couriers".id = "Orders".courierId
WHERE
  "Orders".inDelivery
GROUP BY 1;
