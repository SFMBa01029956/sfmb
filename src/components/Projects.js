import { Container, Row, Col, Nav, Tab } from "react-bootstrap";
import { ProjectCard } from "./ProjectCard";
import colorSharp2 from '../assets/img/color-sharp2.png';
import projImg1 from '../assets/img/project-img1.png';
// import projImg2 from '../assets/img/project-img2.png';
// import projImg3 from '../assets/img/project-img3.png';
import TrackVisibility from 'react-on-screen';

export const Projects = () => {
  const projects = [
    {
      title: "Business Startup",
      description: "Design & Development",
      imgUrl: projImg1,
    }
  ]
  return (
    <section className="project" id="project">
      <Container>
        <Row>
          <Col>
          <TrackVisibility>
            {({ isVisible }) => 
              <div className={isVisible ? "animated__animated animate__slideInUp" : ""}>
            <h2>Projects</h2>
            <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl nec ultricies lacinia, nisl nisl aliquet nisl, nec aliquet nisl nisl sit amet lorem. </p>
            </div>}
            </TrackVisibility>
            <Tab.Container id="projects-tabs" defaultActiveKey="first">
              <Nav variant="pills" className="nav-pills mb-5 justify-content-center align-items-center" id="pills-tab">
                <Nav.Item>
                  <Nav.Link eventKey="first">Tab One</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                  <Nav.Link eventKey="second">Tab Two</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                  <Nav.Link eventKey="third">Tab Three</Nav.Link>
                </Nav.Item>
              </Nav>
              <Tab.Content>
                <Tab.Pane eventKey="first">
                  <Row>
                    {
                      projects.map((project, index) => {
                        return (
                          <ProjectCard
                            key={index}
                            {...project}
                          />
                        )
                      })
                    }
                  </Row>
                </Tab.Pane>
                <Tab.Pane eventKey="second">
                  <Row>
                    {
                      projects.map((project, index) => {
                        return (
                          <p>Lorem Ipsum</p>
                        )
                      })
                    }
                  </Row>
                </Tab.Pane>
                <Tab.Pane eventKey="third">
                  <Row>
                    {
                      projects.map((project, index) => {
                        return (
                          <p>Lorem Ipsum</p>
                        )
                      })
                    }
                  </Row>
                </Tab.Pane>
              </Tab.Content>
            </Tab.Container>
          </Col>
        </Row>
      </Container>
      <img className="background-image-right" src={colorSharp2} alt=""/>
    </section>
  )
}