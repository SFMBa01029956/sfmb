import { Col } from 'react-bootstrap'

export const ProjectCard = ({ title, description, imgUrl, href, onClick}) => {
  return (
    <Col sm={6} md={4}>
      <a href={href} target="_blank" rel="noreferrer" style={{ color: 'inherit', textDecoration: 'none' }} onClick={onClick}>
        <div className="proj-imgbx">
          <img src={imgUrl} alt=""/>
          <div className="proj-txtx">
            <h4>{title}</h4>
            <span>{description}</span>
          </div>
        </div>
      </a>
    </Col>
  )
}