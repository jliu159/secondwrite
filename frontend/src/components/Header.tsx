import React from "react";
import "../styles/header.css";
import { useNavigate } from "react-router-dom";

interface HeaderProps {
  currentStep: string;
}

const Header: React.FC<HeaderProps> = ({ currentStep }) => {
  const steps = [
    { label: "Upload", key: "upload" },
    { label: "Review", key: "review" },
  ];

  const navigate = useNavigate();

  return (
    <header className="progress-header">
      <ul className="progress-steps">
        {steps.map((step) => (
          <div key={step.key} style={{cursor: 'pointer'}} className={"step" + (step.key === currentStep ? " active" : "")} onClick={()=> navigate('/' + step.key)}>
            {step.label}
          </div>
        ))}
      </ul>
    </header>
  );
};

export default Header;
